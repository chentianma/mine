/**
 * Created by ivory on 2017/5/19.
 */
$('.art_list').mouseenter(function () {
        $(this).animate(
            {
                marginLeft: '30px',
                marginRight: '30px'
            },
            "1500"
        )
    }
);

$('.art_list').mouseleave(function () {
        $(this).animate(
            {
                marginLeft: '0px',
                marginright: '0px'
            },
            "fast"
        )
    }
);