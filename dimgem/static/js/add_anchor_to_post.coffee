main = ->

    $(window).load ->
        $('.js-anchor').each ->
            postId = $(@).data('post-id')
            $(".js-anchor[data-post-id=#{postId}]").attr('name', "#{postId}")

$ ->
    main()
