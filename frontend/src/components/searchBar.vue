<template>
	<div class="search bar">
        <form>
            <input type="text" v-bind:placeholder="defaultvalue" name="search" v-model="searchInfo">
            <button @click="iclick"></button>
        </form>
    </div>

</template>


<script type="text/javascript">
export default{
	data(){
		return{
			searchInfo:null,
		}
	},
	props:['defaultvalue'],
	methods:{
		iclick:function(event){
			event.preventDefault();
			this.$emit('trans-info',this.searchInfo);
		}
	}
}
</script>


<style scoped>
*{
	text-align:center;
}
div.search {
	padding:10px;
	float:right;
}
form {
	position:relative;
	width:300px;
	margin:0 auto;
	font-weight:500;
	font-family:"Microsoft YaHei","宋体","Segoe UI","Lucida Grande",Helvetica,Arial,sans-serif,FreeSans,Arimo;
}
.seach input,.search button {
	border:none;
	outline:none;
}
.search input {
	width:100%;
	height:32px;
	padding-left:13px;
}
.search button {
	height:42px;
	width:42px;
	cursor:pointer;
	position:absolute;
}
.bar form {
	height:42px;
}
.bar input {
	text-align:left;
	width:150px;
	border-radius:20px;
	border:2px solid #324B4E;
	background:white;
	transition:.3s linear;
	float:right;
}
.bar input:focus {
	width:200px;
}
.bar button {
	background:none;
	top:-2px;
	right:15px;
}
.bar button:before {
	content:"Search";
	font-family:FontAwesome;
	color:#324b4e;
}
</style>