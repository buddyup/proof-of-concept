var dragDealers = [];

function drag_stopped(id, x, y) {
    console.log(id + ": " + x);
    all_data = []
    var d;
    for (var index in dragDealers) {
        d = dragDealers[index];
        console.log(d)
        all_data.push({
            "pk": d.pk,
            "value": d.instance.getValue()[0]
        });
    }
    console.log(all_data)
    $.post(window.save_sales_url, JSON.stringify(all_data), successful_save, failed_save);
}
function successful_save(data) {
    console.log("all good");
}
function failed_save(data) {
    console.log("Failed!")
}
$(function() {
    $(".dragdealer").each(function() {
        var my_id = $(this).attr("id");
        console.log(my_id + "_x")
        console.log(window[my_id + "_x"])
        var d = new Dragdealer(my_id, {
            'steps': 5,
            'speed': 0.2,
            'loose': true,
            'left': 30,
            'right': 30,
            'x': window[my_id + "_x"],
            'callback': function(x,y) {
                drag_stopped(my_id, x, y);
            }
        });
        dragDealers.push({
            pk: $(this).attr("data-pk"),
            instance: d
        });
    });
});