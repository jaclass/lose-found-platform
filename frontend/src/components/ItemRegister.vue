<template>
	<div>
		<input type="radio" name="ItemType" value="card" id="card" v-model="picked"/><label for="card">校园卡</label>
    	<input type="radio" name="ItemType" value="other" id="other" v-model="picked"/><label for="other">其它物品</label>
		
		<!--校园卡表单-->
		<div v-if="picked==='card'">
			<card-register></card-register>
		</div>
		<!--其他物品表单-->
		<div v-if="picked==='other'">
			<other-register></other-register>
		</div>
	</div>
</template>

<script type="text/javascript">
	import cardRegister from "./cardRegister"
	import otherRegister from "./otherRegister"
	export default{
		data(){
			return {
				picked:'card'
			}
		},
		 components: {
		 	cardRegister,
		 	otherRegister
		 }
	}

</script>

<style scoped>
	*{
		text-align:center
	}
	input{
		margin-top: 30px;
	} 
</style>