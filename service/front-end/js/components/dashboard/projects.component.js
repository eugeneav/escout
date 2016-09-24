import React from "react";
import {Link} from 'react-router';
import Constants from '../../constants';
import {withRouter} from 'react-router'


class Projects extends React.Component {

    constructor() {
        super();
    }

    render() {

        return (<div>
            <div className="list-group">
                <a className="list-group-item active" href="#">Project 1</a>
                <a className="list-group-item" href="#">Project 2<span className="badge">14</span></a>
                <a className="list-group-item" href="#">Project 3<span className="badge">2</span></a>
                <a className="list-group-item" href="#">Project 4<span className="badge">4</span></a>
                <a className="list-group-item" href="#">Project 5<span className="badge">9</span></a>
                <a className="list-group-item" href="#">Project 6</a>
            </div>

            <nav>
                <ul className="pager">
                    <li><a href="#">Previous</a></li>
                    <li><a href="#">Next</a></li>
                </ul>
            </nav>
        </div>);
    }
}

export default withRouter(Projects);