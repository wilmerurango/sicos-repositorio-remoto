$(document).on('ready',funcPrincipal);

function funcPrincipal()
{
  $("BtnAgregar").on('click',funcNuevoAlineamiento);
}

function funcNuevoAlineamiento()
{
  $("#TablaAgregar")
  .append
  (
    $('<tr>')
    .append
    (
      $('<td>')
      .append
      (
        $('<input>').attr('type','Select').addClass('form-control')
      )
    )

    .append
    (
      $('<td>')
      .append
      (
        $('<input>').attr('type','text').addClass('form-control')
      )
    )

    .append
    (
      $('<td>')
      .append
      (
        $('<td>').addClass('text-center')
        .append
        (
          $('<div>').addClass('btn btn-primary').text('Guardar')
           
        )
        .append
        (
          $('<div>').addClass('btn btn-danger').text('Eliminar')
           
        )
      )
    )
    
  )

}
