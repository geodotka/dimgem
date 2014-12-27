showForm = ->
    $('.js-report-mistake-to-post-form').hide()
    $('.js-show-form').click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        $(@).hide()
        $(".js-report-mistake-to-post-form[data-post-id=#{postId}]").show()


clearAndHideForm = (postId) ->
    $form = $(".js-report-mistake-to-post-form[data-post-id=#{postId}]")
    $form.find('#id_author').val('')
    $form.find('#id_email').val('')
    $form.find('#id_text').val('')
    $('.js-show-form').show()
    $(".js-report-mistake-to-post-form[data-post-id=#{postId}]").hide()


reportMistakeToPost = (postId, email, text, userId=null, author=null) ->
    $.ajax({
        url: "/api/report_mistake_to_post",
        dataType: "json",
        type: "POST",
        data: {
            post_id: postId
            email: email
            text: text
            user_id: userId
            author: author
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        success: (data, textStatus, jqXHR) ->
            postId = data['post_id']
            html = "<span class=\"js-note-#{postId}\">Dziękujemy za zgłoszenie błędu</span>"
            $(".js-note[data-post-id=#{postId}]").html(html)
            clearAndHideForm(postId)
    })


main = ->
    showForm()

    $(".js-report-mistake").click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        userId = $('.js-author').data('user-id')
        $form = $(".js-report-mistake-to-post-form[data-post-id=#{postId}]")
        author = $form.find('#id_author').val()
        email = $form.find('#id_email').val()
        text = $form.find('#id_text').val()
        reportMistakeToPost(postId, email, text, userId, author)

    $('.js-cancel').click (ev) ->
        ev.preventDefault()
        postId = $(@).data('post-id')
        clearAndHideForm(postId)


$ ->
    main()
