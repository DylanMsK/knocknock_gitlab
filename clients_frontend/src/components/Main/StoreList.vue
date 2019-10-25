<template>
	<v-list 
		flat 
		class="storelist py-0"
	>
		<v-list-item 
			v-for="(store, idx) in stores"
			:key=idx
			@click="goTo('store-detail', store.id)"
			class="d-block px-0 py-1"
		>
			<div class="store-content">
				<div class="store-title">{{ store.name }}</div>
				<div class="store-subcategory">{{ store.category }}</div>
				<div class="ellipsis">
					<div class="store-remainingtime">마감 {{ store.remainingTime }}분 전</div>
					<v-divider vertical class="divider"></v-divider>
					<div class="store-biztime">{{ store.biztime }}</div>
				</div>
				<div class="ellipsis">
					<div class="store-biztel">{{ store.contact }}</div>
					<v-divider vertical class="divider"></v-divider>
					<div class="store-addr">{{ store.roadAddr }}</div>
				</div>
			</div>
			<v-divider 
				v-if="idx != stores.length -1"
				class="mt-1"
			></v-divider>
		</v-list-item>
	</v-list>
</template>

<script>
import router from '../../router'
import { mapState } from 'vuex'

export default {
	computed: {
		...mapState('store', ['stores'])
	},
	methods: {
		goTo(path, params) {
			router.push({ name: path, params:{ storeId: params} });
    },
	}
}
</script>

<style scoped>
.storelist {
	height: 38vh;
	overflow: auto;
	/* border: 1px solid rgba(0, 0, 0, 0.2) !important;  */
	border-radius: 5px;
}
.store-content {
	padding: 0 15px;
}
.store-title {
	display: inline;
	font-weight: 700; 
}
.store-subcategory {
	display: inline;
	font-size: 14px;
	color: gray;
	padding: 10px 0 0 5px;
}
.store-remainingtime {
	display: inline;
	color: red;
}
.store-biztime {
	display: inline;
	font-size: 14px;
	padding: 0;
}
.store-biztel {
	display: inline;
	font-size: 14px;
}
.store-addr {
	display: inline;
	font-size: 14px;	
	padding: 0;
}
.ellipsis {
	display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
</style>