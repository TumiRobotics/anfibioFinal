class Usuarios extends React.Component
{
    constructor(props)
    {
        super(props)
    }

    componentDidMount()
    {
        setTimeout(()=>{
            $("#img_usr").attr("src","/static/usr/usr-0001.jpeg")
        },2000)
    }

    render()
    {
        return(
            <div className="appLoginStart">
                <img id='img_usr'/>
            </div>
        );
    }
}