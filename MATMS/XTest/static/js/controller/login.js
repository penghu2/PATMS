/**
 * Created by stone on 2015/3/8.
 */
var loginItem = function(){
    function isEmail(strEmail){
        var emailReg = /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/;
        if( emailReg.test(strEmail) ){
        return true;
        }else{
        return false;
        }}

    function isNull( str ){
        if ( str == "" ) return true;
        var regu = "^[ ]+$";
        var re = new RegExp(regu);
        return re.test(str);
    }

    function isUserNameOK(username)
    {
        var regu = "^[0-9a-zA-Z\_]+$";
        var re = new RegExp(regu);
        if (re.test(username)) {
            return true;
        }else{
            return false;
        }
    }

    function isPasswordOK(passwd)
    {
        var regu = "^[0-9a-zA-Z]+$";
        var re = new RegExp(regu);
        if (re.test(passwd)) {
            return true;
        }else{
            return false;
        }
    }

    this.submit = function(user,passwd)
    {
        $.post("../login",
           { username: user, password: passwd },
           function(data){
              //alert("Data Loaded: " + JSON.stringify(data));
              afterConfirm(data);
           },
           'json'
        );
    };

    function afterConfirm(data)
    {
        alert(data);
    }
};

