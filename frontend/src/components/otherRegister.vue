<template>
	<form action="">
		*物品名称 ： <input type="text" name="itemName" v-model="item"/>	<br>
		<p class='info' v-if="item==''">写上物品名称</p>
		<p class='pass' v-if="item!=''"> √ </p>
		*物品描述  :  <textarea v-model="message" placeholder="拾取地点、特征等" ></textarea>
		<p class='info' v-if="message==''">描述一下物品，方便失主筛选^_^</p> <br>
		<p class='pass' v-if="message!=''"> √ </p>
		*联系手机 ： <input type="text" name="teleNo2" v-model="phone"/>  <br>
		<p class='info' v-if="checkTele()==0">手机号码不能为空</p>
		<p class='info' v-if="checkTele()==1">无效手机号码</p>
		<p class='pass' v-if="checkTele()==2"> √ </p>
		*保管方式 ： <input type="radio" name="KeepType2" value="myself" id="myself" v-model="keep"/><label for="myself"> 本人保管 </label>
				   <input type="radio" name="KeepType2" value="toCenter" id="toCenter" v-model="keep"/><label for="toCenter"> 交至失物中心 </label>  <br>
		*日期： <input type="date" name="user_date2" v-model="date"/>  <br>
		<input class="Submit" type="submit" value="提交" @click="warn($event)"/>
	</form>
</template>

<script type="text/javascript">
	export default{
		data(){
			return{
				phone:'',
				message:'',
				item:'',
				keep:'',
				date:''
			}
		},
		computed:{
			getKeep:function(){
				if(this.keep='myself')
					return '本人保管';
				if(this.keep='toCenter')
					return '交至失物中心';
			}
		},
		methods:{
			checkTele:function(){
				var reg=11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/;
				if(this.phone=='')
					return 0;
				else if(!reg.test(this.phone))
					return 1;
				else
					return 2;
			},
			warn: function(event){
				event.preventDefault();
				if(this.checkTele()!=2 || this.message=='' || this.keep=='' || this.date==''){
					alert("信息遗漏或无效！");
				}
				else
					this.$ajax.post('http://127.0.0.1:8000/itemsinfo/',{ params: { 'token': sessionStorage.getItem('token') }},
					{data:{
						itemName:this.item,
						foundTime:this.date,
						keep:this.getKeep,
						status:"未领取",
						phone:this.phone,
						description:this.message
					}}).then(function(){alert("信息提交成功！");  window.history.back();});
			}
		}
		
	}
	
</script>

<style scoped>
	input{
		margin-top:30px;
	}
	.info{
		color:red;
		font-size:5px;
	}
	.pass{
		color:green;
		font-size:8px;
	}
	.Submit{
		font-size:130%;
		background-color:transparent;
		border-width:1px;
		border-color:black;
		border-style:solid;
		border-radius:3px;
	}
	input.Submit:hover{
		background-color:lightgrey;
	}
	textarea{
		width:160px; 
		height:100px; 
		border:solid 1px grey; 
		vertical-align:top; 
		border-radius:10px; 
		resize:none;

	}

</style>