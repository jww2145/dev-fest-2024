/**
* The logistical sub-component of Progress-Bar.svelte
*
* @authors Joshua Wu
*/
<script>
    export let progress = 0;

    
</script>

<div class ="outer">
    <div class ="inner" style="width: {progress * 100}%">{Math.trunc(progress * 100)}%</div>
</div>

<style>
    .inner,.outer{
        height: 20px;
    }

    .outer{
        width:80%;
        margin: 10px auto;
        background-color: transparent;
        border: 1px solid #005682;
    }

    .inner{
        width: 40%;
        background-color: #D8F1FF;
        text-align: center;
        font-family:Georgia;
    }
</style>

