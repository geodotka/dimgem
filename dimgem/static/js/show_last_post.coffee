main = ->
    $('.js-drawer-inside').hide()

    $('.js-drawer-door').click (ev) ->
        category = $(@).data('category')
        dim = $(@).data('type')
        $door = $(".js-drawer-door[data-category=#{category}][data-type=#{dim}]")
        $drawerInside = $door.parent().find('.js-drawer-inside')
        if $door.hasClass('down')
            $door.removeClass('down')
            $door.addClass('up')
        else
            $door.removeClass('up')
            $door.addClass('down')
            if category == 'False'
                category = 'False friends'

            $.ajax({
                url: "/api/show_newest_post"
                dataType: "json"
                type: "POST"
                data:
                    category: category
                    dim: dim
                    csrfmiddlewaretoken: $.cookie('csrftoken')
                success: (data, textStatus, jqXHR) ->
                    if data['success'] == true
                        date = data['date']
                        author = data['author']
                        url = data['url']
                        title = data['title']
                        text = data['text']
                        html = '<div class="container-header">'
                        html += "<h4>#{date} #{author}<br><a href=\"#{url}\">#{title}</a></h4></div><div class=\"container-text post\">#{text}</div></div>"
                        $drawerInside.html(html)
                    else
                        $drawerInside.html('Nie było jeszcze postów w tej kategorii.')
            })
        $drawerInside.slideToggle('slow')


$ ->
    main()
