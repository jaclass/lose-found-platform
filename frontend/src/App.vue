<template>
  <div id='app'>
    <div class='navigation'>
      <ul>
        <li id='nav-icon'><p>Lose&Found  from  Piclass</p></li>
        <li> <router-link to="/list" >待取列表</router-link> </li>
        <li> <router-link to="/register" >登记物品</router-link> </li>
        <li><a href='http://piclass.cn/blog/article/17.html'>@piclass</a> </li>
        <li> <router-link to="/login" >登录/注册</router-link> </li>
      </ul>
    </div>
    <div id='main'>
      <div id='content'>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scope>
.navigation {
  position:fixed;
  left:0px;
  top:0px;
  width:100%;
  height:50px;
  border-bottom:0.5px blue;
  overflow:hidden;
  padding-left:auto;
  padding-right:auto;
  background-color:white;
}
.navigation>ul{
  list-style-type:none;
  padding:0;
  margin:0;
  text-align: center;
}
.navigation>ul>li{
  display:inline-block;
  padding-bottom: 0;
}
.navigation>ul>li>a{
  color:black;
  display:block;
  width:120px;
  background-color:white;
  text-align:center;
  padding:10px;
  font-size: 125%;
  text-decoration:none;
}
.navigation ul>li>a:hover{
  color:grey;
  font-size: 130%;
}
#nav-icon{
  padding-right:30px;
  color:#1E90FF;
  font-weight:bold;
  font-family:Courier New;
  font-size:135%;
}
#main{
  border-radius:8px;
  margin-top:100px;
  margin-bottom:50px;
  width:850px;
  padding-bottom:120px;
  margin-left:auto;
  margin-right:400px;
  background-color:white;
}
</style>
