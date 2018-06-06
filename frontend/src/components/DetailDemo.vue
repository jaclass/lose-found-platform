<template>
<div>
	<div id="globalbackground">	</div>
	<div id="itemdetail">
		<button id="quit" @click="goback">X</button>
		<div id="content">
			<div id="pic"> 图片 </div>
			<div id='text'> <p> <em>物品描述</em> : {{this.content}} </p> </div>
			<p> <em>联系方式</em> : {{this.phone}} </p>
		</div>
	</div>
</div>

</template>



<script type="text/javascript">
export default{
	data(){
		return{
			/*items: [
			{'name':'macbook','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'银色笔记本'},
			{'name':'lenovo1.0','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'蓝色笔记本'},
			{'name':'lenovo2.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'黑色笔记本'},
			{'name':'lenovo3.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'笔记本'},
			{'name':'lenovo4.1','date':'2018/4/2','keep':'交至失物中心','state':'未领取','phone':'13818415318','detail':'彩笔记本'},
			{'name':'lenovo5.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'银色笔记本'},
			{'name':'lenovo6.0','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'用 Vue.js + vue-router 创建单页应用，是非常简单的。使用 Vue.js ，我们已经可以通过组合组件来组成应用程序，当你要把 vue-router 添加进来，我们需要做的是，将组件(components)映射到路由(routes)，然后告诉 vue-router 在哪里渲染它们。下面是个基本例子：'},
			{'name':'lenovo7.2','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'一个笔记本'},
			],
			*/
			content:null,
			phone:null
		}
	},

	
	methods:{
		goback: function(){
			 window.history.back();
		},
		
		init () {
		        this.$ajax.get('http://127.0.0.1:8000/itemsinfo/'+this.$route.params.id,{ params: { 'token': sessionStorage.getItem('token') }}
		        ).then(data => {
		          data = data.data;
		          this.content=data.description;
		          this.phone=data.phone;
		        })
	        },
		
	},

	mounted(){
		this.init();
	},
}
</script>



<style scoped>
	*{
		text-align: left;
		
	}
	#quit{
		float:right;
		background-color:transparent;
		border:none;
		padding:3px;
	}
	button:hover{
		color:red;
	}
	#pic{
		text-align:center;
		width:100px;
		height:100px;
		margin:15px auto;
		border-width:1.5px;
		border-color:black;
		border-style:solid;
	}
	#content{
		padding-top:30px;
	}
	#globalbackground{
		width:100%;
		height:100%;
		position:fixed;
		background-color:grey;
		bottom:0;
		top:0;
		left:0;
		opacity:0.75;
		filter:Alpha(opacity=0.75);
		overflow:hidden;
		z-index:5;
	}
	#itemdetail{
		width:500px;
		background-color:#FFFFFF;
		border-radius:12px;
		padding: 15px;
		padding-top:2px;
		padding-right:2px;
		text-align:left;
		position:absolute;
		left:0; right:0; top:60px; 
		margin:auto;
		z-index:10;
	}
	#text{
		margin:2px;
	}

</style>