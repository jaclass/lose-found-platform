<template>
	<div>
		<div>
	        <search-bar defaultvalue="搜索物品/特征..." v-on:trans-info="childMsg"></search-bar>
	    </div>
		<table id="datalist">
			<thead>
				<tr>
					<th>序号</th>
					<th>物品名称</th>
					<th>拾取日期</th>
					<th>保管方式</th>
					<th>状态</th>
					<th>联系方式</th>
					<th>详情</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(item,index) in items">
					<td>{{index+1}}</td>
					<td>{{item.itemName}}</td>
					<td>{{item.foundTime}}</td>
					<td>{{item.keep}}</td>
					<td>{{item.status}}</td>
					<td v-if="item.keep=='本人保管'">{{item.phone}}</td>
					<td v-else>/</td>
					<td><router-link v-bind:to="'list/detail/'+item.id">详情</router-link></td>
				</tr>
			</tbody>
		</table>
		<router-view></router-view>
	</div>
</template>

<script type="text/javascript">
import searchBar from "./searchBar"
export default{
	data(){
		return{
			/*
			items: [
			{'name':'macbook','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'银色笔记本'},
			{'name':'lenovo1.0','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'蓝色笔记本'},
			{'name':'lenovo2.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'黑色笔记本'},
			{'name':'lenovo3.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'笔记本'},
			{'name':'lenovo4.1','date':'2018/4/2','keep':'交至失物中心','state':'未领取','phone':'13818415318','detail':'彩笔记本'},
			{'name':'lenovo5.1','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'银色笔记本'},
			{'name':'lenovo6.0','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'白色笔记本'},
			{'name':'lenovo7.2','date':'2018/4/2','keep':'本人保管','state':'未领取','phone':'13818415318','detail':'一个笔记本'},
			]
			*/
			items:[],
		}
	},
	components:{
		searchBar
	},
	methods:{
		init () {
		        this.$ajax.get('http://127.0.0.1:8000/itemsinfo/',{ params: { 'token': sessionStorage.getItem('token') }}
		        ).then(data => {
		          data = data.data;
		          this.items=data;
		          //console.log(this.items);
		        })
	        },

        childMsg:function(info){
			this.$ajax.get('http://127.0.0.1:8000/itemsinfomation/search/'+info,{ params: { 'token': sessionStorage.getItem('token') }}
			).then(data => {
				data=data.data;
				if(data.length==0)
					alert("暂无数据！");
				else
					this.items=data;
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