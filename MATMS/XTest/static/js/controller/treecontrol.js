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
