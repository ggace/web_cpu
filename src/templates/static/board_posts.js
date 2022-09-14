class Board extends React.Component {
  constructor(props) {
	    super(props)
	}
	render() {

		const style = {
		}
		return (
  		<div className="board" style={style}>
  			<div style={{"width":"50px"} } id="number">{this.props.boardId}</div>
        <div id="title">{this.props.title}</div>
        <div id="user">{this.props.user}</div>
        <div id="updateDate">{this.props.updateDate}</div>
  		</div>
		);
	}
}
