<template>
	<div id="background">
		<div id="loginMain">
			<button type="button" id="exit" @click="goBack"> X </button>
			<form action="">

				<p>账号： <input type="text" name="account"></p>
				<p>密码： <input type="password" name="password"></p>

				<p><input type="submit" value="登录"></p>
			</form>
			<a href="http://piclass.cn/register.html">还没有Piclass账号？快上车</a>
		</div>
	</div>
</template>

<script type="text/javascript">
	export default{
	  name: 'Login',
	  methods: {
	    goBack () {
	      window.history.back();
	    }
	  }
	}
</script>

<style scoped>
#background{
	width:100%;
	height:100%;
	position:fixed;
	background-color:grey;
	bottom:0;
	top:0;
	opacity:0.75;
	filter:Alpha(opacity=75);
	overflow:hidden;
	z-index:5;
}

#loginMain{
	width:450px;
	height:200px;
	background-color:white;
	border-radius:12px;
	margin:100px auto;
	padding: 30px;
	text-align: center;
	position: relative;
}

#exit{
	position:absolute;
	top:5px;
	right:5px;
	border-width:0px;
	background-color:white;
}
#exit:hover{
	color:red;
}

form{
	margin:20px auto;
}
</style>