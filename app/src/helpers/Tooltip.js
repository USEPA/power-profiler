export { addTooltip }

function addTooltip(className){
    $(className).on({
        mouseover : function() {
          // mouseover event
          var title = $(this).attr('title');

          $(this).data('tipText', title).removeAttr('title');

          $('<p class="tooltip"></p>')
          .text(title)
          .appendTo('#app')
          .fadeIn('fast');
        },
        mouseout : function() {
          // mouseout event
          $(this).attr('title', $(this).data('tipText'));
          var nodes = document.querySelectorAll(".tooltip");
          for(var i = 0; i < nodes.length; i += 1){
            $(nodes[i]).remove()
          }
        },
        mousemove : function(e){
          // Check if element is a national bar (on the righthand side of the page)
          const natBar = $(this).parents('.nationalBar');

          if(natBar.length || e.target.classList.contains("nationalBar")){
            positionTooltip(e, - $(".tooltip").width() - 90, 350);
          } else {
            positionTooltip(e, 0, 350);
          }
        }
    });
}

function positionTooltip(e, x, y){
  var mousex = e.pageX + x; // Get X coordinates
  var mousey = e.pageY - y; // Get Y coordinates

  $('.tooltip')
  .css({top: mousey + 'px', left: mousex + 'px'})
}
