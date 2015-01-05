hideForms = ->
    $('.js-new-text').val('')
    $('.js-refusal-reason').val('')
    $('.js-accept-note-to-post-form').hide()
    $('.js-refuse-note-to-post-form').hide()
    $('.js-cancel').hide()


acceptNote = (noteId, newText) ->
    $.ajax({
        url: "/api/accept_note_to_post",
        dataType: "json",
        type: "POST",
        data: {
            note_id: noteId
            new_text: newText
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        success: (data, textStatus, jqXHR) ->
            if data['success']
                $(".js-note-row[data-note-id=#{noteId}]").remove()
            else
                errors = data['errors'].new_text[0]
                $(".js-text-accept-error[data-note-id=#{noteId}]").html(errors)
    })


refuseNote = (noteId, refusalReason) ->
    $.ajax({
        url: "/api/refuse_note_to_post",
        dataType: "json",
        type: "POST",
        data: {
            note_id: noteId
            refusal_reason: refusalReason
            csrfmiddlewaretoken: $.cookie('csrftoken')
        },
        success: (data, textStatus, jqXHR) ->
            if data['success']
                $(".js-note-row[data-note-id=#{noteId}]").remove()
            else
                errors = data['errors'].refusal_reason[0]
                $(".js-text-refuse-error[data-note-id=#{noteId}]").html(errors)
    })


main = ->
    hideForms()
    $('.js-accept-note').click (ev) ->
        ev.preventDefault()
        noteId = $(@).data('note-id')
        $(".js-refusal-reason[data-note-id=#{noteId}]").val('')
        $(".js-text-refuse-error[data-note-id=#{noteId}]").html('')
        $(".js-accept-note-to-post-form[data-note-id=#{noteId}]").show()
        $(".js-refuse-note-to-post-form[data-note-id=#{noteId}]").hide()
        $(".js-cancel[data-note-id=#{noteId}]").show()
    $('.js-refuse-note').click (ev) ->
        ev.preventDefault()
        noteId = $(@).data('note-id')
        $(".js-new-text[data-note-id=#{noteId}]").val('')
        $(".js-text-accept-error[data-note-id=#{noteId}]").html('')
        $(".js-accept-note-to-post-form[data-note-id=#{noteId}]").hide()
        $(".js-refuse-note-to-post-form[data-note-id=#{noteId}]").show()
        $(".js-cancel[data-note-id=#{noteId}]").show()

    $('.js-accept-note-ok').click (ev) ->
        ev.preventDefault()
        noteId = $(@).data('note-id')
        newText = $(".js-new-text[data-note-id=#{noteId}]").val()
        acceptNote(noteId, newText)

    $('.js-refuse-note-ok').click (ev) ->
        ev.preventDefault()
        noteId = $(@).data('note-id')
        refusalReason = $(".js-refusal-reason[data-note-id=#{noteId}]").val()
        refuseNote(noteId, refusalReason)

    $('.js-cancel').click (ev) ->
        ev.preventDefault()
        noteId = $(@).data('note-id')
        $(".js-new-text[data-note-id=#{noteId}]").val('')
        $(".js-refusal-reason[data-note-id=#{noteId}]").val('')
        $(".js-accept-note-to-post-form[data-note-id=#{noteId}]").hide()
        $(".js-refuse-note-to-post-form[data-note-id=#{noteId}]").hide()
        $(".js-cancel[data-note-id=#{noteId}]").hide()

$ ->
    main()
