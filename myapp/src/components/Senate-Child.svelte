<script>
    import Senators from "./Senators.svelte";

</script>

<div class = 'container'>
    <div class = 'container-child-left'>Test Test</div>
    <div class = 'container-child-right'><Senators /></div>
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
        width: 27%;
        padding:3%;
        background-color: rgb(216, 241, 255,.5);
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size:12pt;
        text-align:center;
        border: 1px solid #005682;
    }

    .container-child-right{
        width: 60%;
        padding: 1%;
        background-color:rgb(216, 241, 255,.5);
        font-family: Georgia, 'Times New Roman', Times, serif;
        font-size: 12pt;
        text-align: center;
        border: 1px solid #005682;
    }
</style>