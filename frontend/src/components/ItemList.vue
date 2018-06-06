<template>
	<div>
		<input type="radio" name="ListType" value="cardList" id="cardList" v-model="type_of_list"/><label for="cardList">校园卡</label>
		<input type="radio" name="ListType" value="otherList" id="cardList" v-model="type_of_list"/><label for="otherList">其它待取物品</label>
		<div v-if="type_of_list==='cardList'">
			<card-list></card-list>
		</div>
		<div v-if="type_of_list==='otherList'">
			<other-list></other-list>
		</div>
	</div>
</template>



<script type="text/javascript">
	import cardList from "./cardList"
	import otherList from "./otherList"
	export default{
		data(){
			return{
				type_of_list:'cardList'
			}
		},
		components:{
			cardList,
			otherList
		}
	}
</script>



<style scoped>
	*{
		text-align:center;
	}
</style>