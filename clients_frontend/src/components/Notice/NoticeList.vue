<template>
	<v-container>
		<p class="font-headline">공지사항</p>
		<v-list>
      <v-list-group 
				v-for="(item, idx) in items"
				:key="idx"
				no-action
				class="list-group-border"
			>
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title style="overflow: visible; white-space: inherit;">
							{{ item.title }}
						</v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item class="pl-6">
          <v-list-item-content>
						{{ item.content }}
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
	</v-container>
</template>

<script>
export default {
	data() {
		return {
			items: [
				{
					'title': '[공지] 모든 가게의 운영시간 확인이 가능합니다.',
					'content': '안녕하세요. 낰낰입니다.더욱 편리하게 낰낰을 이용할 수 있도록 웹 서비스가 변경되어 안내 드립니다.'
				},
				{
					'title': '[공지] 개인정보처리방침 일부 변경에 관한 안내',
					'content': '안녕하세요. 낰낰입니다. 게인정보처리방침을 일부 변경하게 되어 이를 알려 드리고자 합니다.'
				},
				{
					'title': '[공지] 시스템 점검 안내',
					'content': '안녕하세요. 낰낰입니다. 2019년 10월 24일 시스템 점검이 진행될 예정으로 안내해드립니다. 점검 중에는 낰낰 웹 및 전체 서비스 이용이 제한되오니 이용에 참고해 주시기 바랍니다.'
				},

			]
		}
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
.list-group-border {
	border-bottom: 0.5px solid rgba(0, 0, 0, 0.3);
}
</style>