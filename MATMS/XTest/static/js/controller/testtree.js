/**
 * Created by stone on 2015/3/9.
 */
var TestTree = function(){

    this.getTree = function(treeID){
        $.get("/ATMS/getTestTree/"+treeID,
            function(result){
                $("div").html(result);
            });
    }
};