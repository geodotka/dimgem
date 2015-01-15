main = ->

    $('.js-resized-picture').mouseover (ev) ->
        src = $(@)[0].src
        $("body").append("<p id='preview'><img src='#{src}' class='picture-previev' alt='Image preview' /></p>")
        $("#preview").css("max-height", "400px").css("max-width", "400px")
        if $(@).data('post-picture')
            $("#preview").css("top", ev.pageY + "px").css("left", (ev.pageX) + "px").fadeIn("fast")
        else
            $("#preview").css("top", ev.pageY + "px").css("right", (ev.pageX - 700) + "px").fadeIn("fast")

    $('.js-resized-picture').mouseout (ev) ->
        $("#preview").remove()


$ ->
    main()
