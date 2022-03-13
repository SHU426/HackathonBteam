//nameが空の時は要素数＋1した値をつける,上記だとlet tailnum=要素数2+1=3, ()->003
//1.送信ボタンをclick->
$('.js-btn-event').on('click', function (e) {
    e.preventDefault(); //submitがキャンセルされる。
    //random関数
    function getRandomArbitrary(min, max) {
        return Math.random() * (max - min) + min;
    }
    //ゼロ埋め
    function zeroPadding(NUM, LEN) {
        return (Array(LEN).join('0') + NUM).slice(-LEN);
    }

    let username = "名無し";
    let img_path = ['./dist/images/sns-icon-man_1.png', './dist/images/sns-icon-man_2.png',
        './dist/images/sns-icon-man_3.png'
    ];

    let ranNum = Math.floor(getRandomArbitrary(1, img_path.length));
    console.log(ranNum);
    let setPath = img_path[ranNum];
    console.log(setPath);
    // inputの値を取得し、中身を空にする
    let text = $('.js-get-value').val();
    $('.js-get-value').val('');
})

//ゴミ箱アイコンclickイベント
// $(".js-click-trash").click(function () {
//     window.location.href = "{% url 'msg_delete' sredmodel.id %}";

// });