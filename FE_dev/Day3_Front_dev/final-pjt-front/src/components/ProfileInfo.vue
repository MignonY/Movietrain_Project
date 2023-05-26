<template>
  <div class="profileinfo">
    <div class="CT_all">
      <div id=pimage>photo 
        <!-- <img class= "photo" src=""> -->
      </div>
      <div id=Pbutton>ICON</div>
      <span id="nickname">USER_NICKNAME</span>
      <h3 id="bg">ProfileBGimage</h3>
      <div class="CT_info">
        <h3 id="info">ProfileInfo</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'ProfileInfo'
}
</script>

<style scoped>
#bg{
  width: 100%;
  height: 14rem;
  background-color:lightgray;
  margin-right: auto;
  margin-left: auto;
  margin-bottom: 0;
  text-align: center;
  line-height: 14rem;
}
#pimage{
  position: absolute;
  left:2rem;
  top:7rem;
  width: 15rem;
  height: 15rem;
  border-radius: 70%;
  overflow:hidden;
  line-height: 15rem;
  background-color: palevioletred;
}
#Pbutton{
  position: absolute;
  left:12.75rem;
  top:16rem;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: 70%;
  overflow:hidden;
  line-height: 4.5rem;
  background-color: rgb(23, 38, 74);
  color:white;
}
.photo{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
#nickname{
  position:absolute;
  font-size: 3.5rem;
  font-weight: 800;
  color:black;
  left:20rem;
  top:13rem;

}
#info{
  width: 100%;
  height: 4rem; 
  background-color:lightsteelblue;
  margin-right: auto;
  margin-left: auto;
  margin-top: 0;
  text-align: center;
  line-height: 4rem;
}
</style>