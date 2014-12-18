dimOrGem = (dimgem_type) ->
    $(dimgem_type).click (ev) ->
        ev.preventDefault()
        $(@).tab()


main = ->
    $dimgem_type = $('.js-tab')
    dimOrGem($dimgem_type)


$ ->
    main()
