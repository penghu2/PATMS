/**
 * Created by stone on 2015/3/9.
 */
var TestTree = function(treeName){

    this.treeObj =  $.fn.zTree.getZTreeObj(treeName);

    this.getTree = function(treeID){
        $.get("/ATMS/UnitTest/detial/"+treeID,
            function(result){
                $.fn.zTree.init($("#treeDemo"), setting, zNodes);
            });
    };

    this.getSelectTree = function(){
        return this.treeObj.getCheckedNodes(true);
    };

};


$("#startTest").click(function(){
    var testtree = new TestTree('treeDemo');
    var nodes = testtree.getSelectTree();
    //alert(JSON.stringify(nodes));
    $("#testresultdiv").html("update.....");
    $.post('/ATMS/UnitTest/detial/1/',
        nodes,
        function(result)
        {
            if(result.status=='0000'){
                var text = result.data;
                $("#testresultdiv").html(text);
            }
        },
        'json'
    );

});