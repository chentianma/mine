/**
 * Created by ivory on 2017/5/19.
 */

var categoryVM = new Vue({
        el: '#categoryTemp',
        data: {
            categories: {},
        },
    }
);

var topicVM = new Vue({
    el: '#topicTemp',
    data: {
        topics: {}
    },
    ready: function () {
        $('.uk-accordion-content').first().show()
    }
    ,
    methods: {
        click_topic: function ($event) {
            el_clicked = $($event.currentTarget).next();
            $('.uk-accordion-content').not(el_clicked).hide(250);
            el_clicked.toggle(250);

        }
    },


});

function getCategories_and_Topics() {
    $.get('/api/categories',
        function (data, status) {
            categoryVM.categories = data.categories
        });
    $.get('/api/topics',
        function (data, status) {
            topicVM.topics = data.topics
        });
};

getCategories_and_Topics();
