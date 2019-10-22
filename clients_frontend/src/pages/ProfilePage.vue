<template>
	<div>
		<div>
			<v-text-field 
				outlined
				value="이혜희"
				clearable
				class="profile-textfield"
			>
			</v-text-field>
			<v-btn text block class="font-weight-bold">
				수정
			</v-btn>
		</div>
		<div class="divide-box"></div>
		<div class="px-8">
			<v-row>
				<v-col 
					cols="4"
					class="font-weight-bold"
				>
					이메일
				</v-col>
				<v-col 
					cols="8"
					class="charcoal--text"	
				>
					lhh9577@navar.com
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="4"
					class="font-weight-bold"
				>
					비밀번호
				</v-col>
				<v-col 
					cols="8"
					class="py-0 d-flex"	
				>
					<v-text-field 
						filled
						dense
						single-line
						type="password"
						placeholder="6자 이상"
					>
					</v-text-field>
					<v-btn 
						depressed 
						tile 
						dark 
						color="grey darken-1"
						class="profile-btn ml-2"
					>
						변경
					</v-btn>
				</v-col>
			</v-row>
		</div>
		<div class="positon-bottom">
			<v-btn 
				text
				class="charcoal--text"
			>
				로그아웃
			</v-btn>
			<v-btn 
				text
				class="charcoal--text"
			>
				회원탈퇴
			</v-btn>
		</div>
	</div>
</template>

<style scoped>
.divide-box {
	width: 100%; 
	height: 30px; 
	background-color: whitesmoke;
	margin: 20px 0;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
.profile-textfield {
	height: 60px;
	margin: 24px 36px 0 36px;
}
.profile-btn {
	height: 40px !important;
}
.positon-bottom {
	position: absolute;
	bottom: 5px;
	right: 5px;
}
</style>