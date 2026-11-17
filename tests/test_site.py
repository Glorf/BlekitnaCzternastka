"""Testy strony: python -m unittest discover tests"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app import app, load_site  # noqa: E402

PAGES = ["/", "/druzyny/", "/oboz/", "/archiwum/", "/kontakt/", "/procent/"]


class DataTests(unittest.TestCase):
    """Błędy w data/site.yml (np. dwukropek w tekście zamienia go w słownik) wychodzą tu, a nie na stronie."""

    def setUp(self):
        self.site = load_site()

    def test_texts_are_strings(self):
        for p in self.site["szczep"]["kim"] + self.site["archiwum"]["wstep"]:
            self.assertIsInstance(p, str)
        for q in self.site["faq"]:
            self.assertIsInstance(q["pytanie"], str)
            self.assertIsInstance(q["odpowiedz"], str)
        for d in self.site["druzyny"] + self.site["instruktorzy"]:
            for p in d["tekst"]:
                self.assertIsInstance(p, str, d["id"])

    def test_teams_have_contact_and_files(self):
        ids = [d["id"] for d in self.site["druzyny"] + self.site["instruktorzy"]]
        self.assertEqual(len(ids), len(set(ids)), "powtórzone id drużyny")
        for d in self.site["druzyny"]:
            self.assertTrue(d["druzynowy"]["telefon"], d["id"])
            self.assertTrue(d["druzynowy"]["email"], d["id"])
            self.assertLess(d["kol"], len(self.site["grupy"]), d["id"])
        for d in self.site["druzyny"] + self.site["instruktorzy"]:
            self.assertTrue((ROOT / "static/img" / d["zdjecie"]).exists(), d["id"])
            if d.get("logo"):
                self.assertTrue((ROOT / "static/img/logo" / d["logo"]).exists(), d["id"])

    def test_archive_links(self):
        for k in self.site["archiwum"]["zbiory"]:
            for l in k["linki"]:
                self.assertTrue(l["url"].startswith("http"), l["tytul"])


class PageTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_pages_render(self):
        for path in PAGES:
            r = self.client.get(path)
            self.assertEqual(r.status_code, 200, path)
            self.assertIn("<title>", r.get_data(as_text=True), path)

    def test_internal_links_resolve(self):
        for path in PAGES:
            html = self.client.get(path).get_data(as_text=True)
            for url in re.findall(r'(?:href|src)="(/[^"#?]*)', html):
                self.assertEqual(self.client.get(url).status_code, 200, f"{path} -> {url}")

    def test_teams_page_has_all_teams_and_tel_links(self):
        html = self.client.get("/druzyny/").get_data(as_text=True)
        site = load_site()
        for d in site["druzyny"] + site["instruktorzy"]:
            self.assertIn(f'id="{d["id"]}"', html)
        for d in site["druzyny"]:
            tel = "tel:" + re.sub(r"[^\d+]", "", d["druzynowy"]["telefon"])
            self.assertIn(f'href="{tel}"', html, d["id"])

    def test_kluszyn_not_in_homepage_hexes(self):
        self.assertNotIn("Kłuszyn", self.client.get("/").get_data(as_text=True))

    def test_menu(self):
        html = self.client.get("/oboz/").get_data(as_text=True)
        nav = re.search(r"<nav>(.*?)</nav>", html, re.S).group(1)
        for label in ["Drużyny", "Obóz", "Archiwum", "Kontakt", "Przekaż"]:
            self.assertIn(label, nav)
        self.assertNotIn(">Start<", nav)

    def test_faq_and_procent(self):
        self.assertIn("Najczęstsze pytania", self.client.get("/kontakt/").get_data(as_text=True))
        html = self.client.get("/procent/").get_data(as_text=True)
        self.assertIn(load_site()["procent"]["krs"], html)


if __name__ == "__main__":
    unittest.main()
