main = ->
    $('.js-remove-picture').hide()

    $(document).on 'change', '#id_picture', (ev) ->
        $('.js-remove-picture').show()

    $(document).on 'click', '.js-remove-picture', (ev) ->
        ev.preventDefault();
        $('.js-load-picture').children().remove()
        $('.js-load-picture').append('<input id="id_picture" type="file" name="image_file">')
        $('.js-remove-picture').hide()


$ ->
    main()
