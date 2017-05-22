/**
 * Created by ivory on 2017/5/19.
 */

var editor_vm = new Vue({
    el: '#editor',
    data: {
        blog: {
            'id': null,
            'url': null,
            'title': null,
            'text': '',
            'time': null,
            'user': null,
            'new_category': null,
            'category': null,
            'description': '',
            'img_url': null
        },
        markhtml: ''
    },
    computed: {
        compiledMarkdown: function () {
            this.markhtml = marked(this.blog.text, {sanitize: true});
            return this.markhtml
        }
    },
    methods: {
        submit_edit: function () {
            this.blog.text = $('#editor_string').val();
            this.blog.category = $("#cate option:selected").text();
            $.post('/api/blog/' + this.blog.id + '/edit', this.blog, function (data, status) {
                var blog_id = data.id;
                $(location).attr('href', '/blog/' + blog_id);
            });
        }
    }
});

function initPage(htmleditor) {
    var path = window.location.pathname;
    $.get('/api' + path, function (data, status) {
        editor_vm.blog = data.blog;
        htmleditor.editor.setValue(editor_vm.blog.text);
    });
};

$(document).ready(function () {
        // {#初始化codemirror编辑器#}
    var mytextarea = document.getElementById('editor_string');
    var htmleditor = UIkit.htmleditor(mytextarea, {mode: 'split', markdown: true});
    initPage(htmleditor);
});





