var getRandomInt = function(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
var month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var historyChart,donutChart,tempX,tempY,inDonut=false;
$(function() {
    historyChart = Morris.Area({
        element: 'history-chart',
        data: [],
        xkey: 'Label',
        ykeys: ['Value'],
        labels: ['$'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true,
        fillOpacity : 0.3 ,
        gridTextColor : '#f5f5f5',
        goalLineColors : ['#eee'],
        lineColors     : ['#fff'],
        parseTime : false,
        hoverCallback : function(index, options, content, row){
            return '$'+parseFloat(row.Value).toFixed(2)+"<br>"+ row.Label;
        }
    });

    loop();
    setInterval(loop,1000 * 60);



    $(document).mousemove(function (e) {
        var bodyOffsets = document.body.getBoundingClientRect();
        tempX = e.pageX - bodyOffsets.left;
        tempY = e.pageY;
    });

});


var loop = function(){
    var data_bar = function(){
        var  array = [];
        for(i=0;i<10;i++)
            array[i] = getRandomInt(1000, 15000);
        return array;
    }
    $.ajax({
        url: 'http://api.uat.didgeepop.com/data/user/summary',
        type: "GET",
        dataType: "json",
        success: function (data) {
            if(!data.success){
                console.log('summary return false');
            }
            
            var array = {
                'receipts' : [],
                'total-spend' : [],
                'monthly' : []
            },
            options = {
                width: '100%',
                height:'77px',
                fill:function(){return'#9e9d9d'}
            };

            $(".receipts .huge").html(data.data.summary.totalReceipts);
            $(".total-spend .huge").html('$'+data.data.summary.totalValue.toFixed(2));
            $(".monthly-spend .huge").html('$'+data.data.summary.montlyVariance.toFixed(2));

            for(key in data.data.trends){
                array['receipts'].push(data.data.trends[key].receipts);
                array['total-spend'].push(parseFloat(data.data.trends[key].value).toFixed(2));
                array['monthly'].push(parseFloat(data.data.trends[key].average).toFixed(2));
            }

            $("#receipts-chart").html(array['receipts'].join(',')).peity("bar", options );

            $("#total-spend-chart").html(array['total-spend'].join(',')).peity("bar", options );

            $("#monthly-spend-chart").html(array['monthly'].join(',')).peity("bar", options);

            $('.peity rect').tipsy({title: 'data-value',gravity: 'w'});
        }
    });





    // history
    $.ajax({
        url: 'http://api.uat.didgeepop.com/data/user/history',
        type: "GET",
        dataType: "json",
        success: function (data) {
            var array = [],
                i     = 0;
            if(!data.success){
                console.log('history return false');
            }

            for(key in data.data.history){
                array[i] = {
                    Value : parseFloat(data.data.history[key].Value).toFixed(2),
                    Label : month[  data.data.history[key].Month - 1 ]  + ' ' + data.data.history[key].Day  
                }
                i++;
            }
            historyChart.setData(array);
        }

    });


    var breakdownArray = [];
    var getBreakdownInfo = function(id,value,total){
        var colors = ['#F79646','#FEC436','#e75849'];
        $.getJSON( "http://cdn.dreceiptx.net/merchant/location/"+id+'/info.json', function( sub_data ) {
                breakdownArray.push({
                    label : '',
                    text  : sub_data.merchantfullname +'<br>'+ sub_data.address.buildingnumber + ' '+ sub_data.address.streetnumber +' '+ sub_data.address.street + '<br>'+ sub_data.address.city
                      +' '+sub_data.address.state +' '+ sub_data.address.postcode + ' ' + sub_data.address.country ,
                    value : value
                })
                // we have all the data at this point , let me the donut
                if(total == breakdownArray.length){
                    if(!donutChart){
                        donutChart = Morris.Donut({
                            element: 'morris-donut-chart',
                            data: breakdownArray,
                            resize: true,
                            colors : colors
                        });  
                        donutChart.on('hover', function(i, row) {
                            $("#donut-text").html(row.text);
                        })
                        $( "#morris-donut-chart path[fill!=none]" ).mousemove(function(e ) {
                            inDonut = true;
                            $("#donut-text").css({'top':tempY+30,'left':tempX-50}).show();

                        });
                        var lastTimeout;
                        $( "#morris-donut-chart path[fill!=none]" ).mouseleave(function(e ) {
                            inDonut = false;
                            lastTimeout = setTimeout(function(){
                                clearTimeout(lastTimeout); 
                                if(!inDonut){
                                   $("#donut-text").hide();
                                   
                                }
                            },500) 
                            
                        })
                        

                    }else{
                        donutChart.setData(breakdownArray);
                    }
                }

        })

    }
    $.ajax({
        url: 'http://api.uat.didgeepop.com/data/user/breakdown',
        type: "GET",
        dataType: "json",
        success: function (data) {
            if(!data.success){
                console.log('breakdown return false');
            }
            var total = Object.keys(data.data.breakdown.merchants).length;
            for(key in data.data.breakdown.merchants){
                getBreakdownInfo(key,data.data.breakdown.merchants[key],total);        
                
            }
        }

    })

    $.ajax({
        url: 'http://api.uat.didgeepop.com/data/user/budget',
        type: "GET",
        dataType: "json",
        success: function (data) {
            if(!data.success){
                console.log('budget return false');
            }
            
            budget('weekly_budgets',data.data.budget.weekly.actual,data.data.budget.weekly.target);
            budget('monthly_budgets',data.data.budget.monthly.actual,data.data.budget.monthly.target);
        }
   
    })
}