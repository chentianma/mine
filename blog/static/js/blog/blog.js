/**
 * Created by ivory on 2017/5/19.
 */
var art_vm = new Vue({
    el: '#article',
    data: {
        blog: {},
        markhtml: '',
        parsedDate: null
    },
    computed: {
        parseDate: function () {
            this.parsedDate = moment(this.blog.time).format('YYYY-MM-DD HH:MM');
            return this.parsedDate
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