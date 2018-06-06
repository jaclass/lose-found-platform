<template>
	<div>
		<div>
	    	<search-bar defaultvalue="搜索卡号" v-on:trans-info="childMsg"></search-bar>
		</div>
		<table id="datalist">
			<thead>
				<tr>
					<th>序号</th>
					<th>校园卡号</th>
					<th>拾取日期</th>
					<th>保管方式</th>
					<th>状态</th>
					<th>联系方式</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(card,index) in cards">
					<td>{{index+1}}</td>
					<td>{{card.cardNo}}</td>
					<td>{{card.foundTime}}</td>
					<td>{{card.keep}}</td>
					<td>{{card.status}}</td>
					<td v-if="card.keep=='本人保管'">{{card.phone}}</td>
					<td v-else>/</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script type="text/javascript">
import searchBar from "./searchBar"
export default{
	data(){
		return{
			/*
			cards: [
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'交至失物中心','state':'未领取','phone':'13818415318'},
			{'id':'10163857','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318'},
			]
			*/
			cards:[],
		}
	},
	//props:['searchId'],
	components:{
		searchBar
	},
	methods:{
			
			init () {
		        this.$ajax.get('http://127.0.0.1:8000/cardsinfo/',{ params: { 'token': sessionStorage.getItem('token') }}
		        ).then(data => {
		          data = data.data;
		          this.cards=data;
		        })
	        },	
	        
	        childMsg:function(info){
				this.$ajax.get('http://127.0.0.1:8000/cardsinfo/'+info,{ params: { 'token': sessionStorage.getItem('token') }}
				).then(data => {
					data=data.data;
					/*if(typeof data == 'object')
					{
						this.cards.length=0;
						this.cards.push(data);
					}
					else */
					this.cards=data;
				}).catch(function(event){
					//console.log("no such info");
					alert("暂无该记录！");
				})
			}
   },
	
	mounted(){
		this.init();
	}

}
</script>

<style scoped>
	table{
		width:800px;
		margin:0 auto;
		border-collapse:collapse;
	}
	td,th{
		border:1px solid lightgrey;
	}
	tr:nth-child(even) td {
		background-color:#EBEBEB;
	}
	thead{
		background-color:lightgrey;
	}
</style>