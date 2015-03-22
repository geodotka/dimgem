showForm = ->
    $('.js-change-post-text-form').hide()
    $('.js-change-post-text').val('')
    $('.js-change-post-text-show-form').click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        $(@).hide()
        $(".js-change-post-text-form[data-post-id=#{postId}]").show()



clearAndHideForm = (postId) ->
    $form = $(".js-change-post-text-form[data-post-id=#{postId}]")
    $form.find('.js-change-post-text').val('')
    $('.js-change-post-text-show-form').show()
    $('.js-change-post-text-error').html('')
    $form.hide()


main = ->
    showForm()

    $(".js-change-post-text-button").click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        postText = $(".js-change-post-text[data-post-id=#{postId}]").val()
        $.ajax({
            url: "/api/change_post_text",
            dataType: "json",
            type: "POST",
            data: {
                post_id: postId
                post_text: postText
                csrfmiddlewaretoken: $.cookie('csrftoken')
            },
            success: (data, textStatus, jqXHR) ->
                postId = data['post_id']
                if data['success']
                    location.reload();
                    clearAndHideForm(postId)
                else
                    if data['error']
                        $('.js-change-post-text-error').html(data['error'])
            error: (jqXHR, textStatus, errorThrown) ->
                $('.js-change-post-text-error').html('Wystąpił nieoczekiwany błąd.')
        })

    $('.js-change-post-text-cancel').click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        clearAndHideForm(postId)


$ ->
    main()
