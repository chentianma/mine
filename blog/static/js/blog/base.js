/**
 * Created by ivory on 2017/5/19.
 */

var categoryVM = new Vue({
        el: '#categoryTemp',
        data: {
            categories: {}
        },
    }
);

function getCategories() {
    $.get('/api/categories',
        function (data, status) {
            categoryVM.categories = data.categories
        })
};

$(document).ready(getCategories())