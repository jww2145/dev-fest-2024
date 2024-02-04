/**
* This component is our amazing header that introduces ourselves!
*
* @authors Joshua Wu and Brian Echvarria
*/
<div class = 'header'></div>
<p class = 'intro'>Created for DevFest 2024</p>
<h1>Environmental Politics by the Numbers</h1>
<p class = 'intro'>By <b>Joshua Wu</b> and <b>Brian Echavarria</b></p>
<div class = 'header'></div>


<style>
    h1{
        color: black;
        font-family: Georgia;
        text-align: center;
    }

    .header{
        margin: auto;
        padding-bottom: 3%;
    }

    .intro{
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        color: black;
        font-size: smaller;
    }

    :global(b){
        font-weight: 1500;
        color: #005682;
    }

    :global(::selection) {
        background: #D8F1FF;
    }
</style>