/**
 * Created by ivory on 2017/5/19.
 */
        var vm = new Vue({
            el: '#art',
            data: {
                blogs: []
            },

            methods: {
                delete_blog: function (blog, index) {
                    if (UIkit.modal.confirm('确认要删除“' + blog.title + '”？删除后不可恢复！',
                                    function () {
                                        $.get('/api/blog/' + blog.id + '/delete', initPage);
                                    }));
                }
            }
        });

        function initPage() {
            $.get('/api/blogs', function (data, status) {
                vm.blogs = data.blogs;
            })
        }

        initPage()