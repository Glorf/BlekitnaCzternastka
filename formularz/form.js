$(document).ready(function(){
  $('#formularz_kontaktowy').bootstrapValidator({
    feedbackIcons: {
      valid: 'glyphicon glyphicon-ok',
      invalid: 'glyphicon glyphicon-remove',
      validating 'glyphicon glyphicon-refresh'
    },
    fields: {
      wiek: {
        validators: {
          
        }
      }
    }
  })
})
