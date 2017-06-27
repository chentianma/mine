/**
 * Created by ivory on 2017/5/19.
 */
vm = new Vue({
    el: '#editor',
    data: {
        blog: {
            'id': null,
            'url': null,
            'title': null,
            'text': '',
            'time': null,
            'user': null,
            'category': null,
            'topic': null
        },
        markhtml: ''
    },
    computed: {
        // compiledMarkdown: function () {
        //     this.markhtml = marked(this.blog.text, {sanitize: true});
        //     return this.markhtml
        // }
    },
    methods: {
        submit_edit: function () {
            this.blog.category = $("#cate option:selected").text();
            this.blog.topic = $("#topic_select option:selected").text();
            this.blog.text = $('#editor_string').val();
            this.blog.html = $('.uk-htmleditor-preview').html();
            $.post('/api/blog/create', this.blog,
                function (data, status) {
                    var blog_id = data.id;
                    $(location).attr('href', '/blog/' + blog_id);
                });
        }
    }
})