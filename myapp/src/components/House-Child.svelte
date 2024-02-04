<script>
    import HouseReps from "./House-Reps.svelte";

</script>

<div class = 'container'>
    <div class = 'container-child-left'>
        <HouseReps/>
    </div>
    <div class = 'container-child-right'>        <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ipsum sodales lacus placerat 
        ultricies in a augue. Vivamus lobortis quam eu tempus porta. Cras ut ex quis tellus rutrum sagittis. 
        Duis at rutrum neque. Vivamus varius felis sed pulvinar venenatis. Cras hendrerit gravida enim, in pulvinar 
        ex aliquam id. Aliquam ipsum leo, ultricies in tortor vel, aliquet feugiat ligula.

        Donec rhoncus ut tellus in suscipit. Proin rutrum sit amet elit eu ornare.
        Donec sed mi gravida, scelerisque dolor sit amet, ornare felis. Fusce vestibulum, 
        ipsum nec aliquam dictum, purus ante facilisis odio, ut tincidunt erat dui nec sem. Morbi eu libero mollis, 
        porttitor felis et, pulvinar odio. Suspendisse eget nibh vitae purus maximus congue ac eu eros. Vestibulum quis 
        massa vitae lacus molestie pretium. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac 
        turpis egestas. Vestibulum eu diam nec ex aliquet pulvinar. Sed ac condimentum metus, in vulputate purus. Nunc in
        metus mollis leo tempus luctus. Curabitur consectetur aliquam elit. Maecenas non ullamcorper neque.
      </p> </div>
</div>

<style>

.container{
        display:flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-around;
        align-items: center;
        align-content: center;
    }

    .container-child-left{
        width: 60%;
        padding:1%;
        background-color: none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size:12pt;
        text-align:center;
        border: none;
    }

    .container-child-right{
        width: 27%;
        padding: 3%;
        background-color:none;
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 12pt;
        text-align: center;
        border: none;
    }

    p{
        line-height: 130%;
    }
</style>