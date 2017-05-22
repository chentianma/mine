/**
 * Created by ivory on 2017/5/19.
 */
var art_vm = new Vue({
    el: '#article',
    data: {
        blog: {},
        markhtml: ''
    },
    computed: {
        compiledMarkdown: function () {
            this.markhtml = marked(this.blog.text);
            return this.markhtml;

        }
    }
});

function initPage() {
    var path = window.location.pathname;
    $.get('/api' + path, function (data, status) {
        art_vm.blog = data.blog;
    });
}
;

$(document).ready(initPage());