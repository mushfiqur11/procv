import React from 'react';
import './App.css';
import { Form, Button, Container, Row, Col } from 'react-bootstrap';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';

// import 'bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component{


  constructor(props) {
    super(props);
    this.state = {
      "username": '',
      "password": '',
      "name": '',
      "email": '',
      "phone": '',
      "github": '',
      "city": '',
      "profileImg": '',
      "coverImg": '',
      "thumbnailImg": '',
      "bio": '',
      // "template": '',

      "projects": [{       
          "project_type": " ",
          "title": " ",
          "sub_heading": " ",
          "short_desc": " ",
          "long_desc": " ",
          "tags": " ",
          "thumb_img": " ",
          "main_img": " ",
          "other_media": " ",
          "other_media_title": " ",
          "code": " ",
          "paper": " ",
          "app": " ",
          "other_link": " ",
          "other_link_title": " ",
          "visible": true
      }],

      "education": [{
      "experience_type": " ",
      "title": " ",
      "start_date": "",
      "end_date": "",
      "position": " ",
      "role": " ",
      "desc": " ",
      "image": " ",
      "employer": " ",
      "employer_link": " ",
      "supervisor": " ",
      "supervisor_link": " ",
      "visible": true
    }],
      
      experience: [{ "experience_type": " ",
      "title": "",
      "start_date": "",
      "end_date": "",
      "position": "",
      "role": "",
      "desc": " ",
      "image": " ",
      "employer": " ",
      "employer_link": " ",
      "supervisor": " ",
      "supervisor_link": " ",
      "visible": true
}],
      "skills":[{      "skill_name": ""}]
    };
  }

  // Projects
  handleAddProject = () => {
    const projects = [...this.state.projects];
    projects.push({
      "project_type": " ",
      "title": " ",
      "sub_heading": " ",
      "short_desc": " ",
      "long_desc": " ",
      "tags": " ",
      "thumb_img": " ",
      "main_img": " ",
      "other_media": " ",
      "other_media_title": " ",
      "code": " ",
      "paper": " ",
      "app": " ",
      "other_link": " ",
      "other_link_title": " ",
      "visible": true
    });
    this.setState({ projects });
  };

  handleProjectChange = (index, key, value) => {
    const projects = [...this.state.projects];
    projects[index][key] = value;
    this.setState({ projects });
  };
  
  // Education
  handleAddEducation = () => {
    const education = [...this.state.education];
    education.push( {
      "experience_type": " ",
      "title": " ",
      "start_date": "2023-04-09",
      "end_date": "2023-04-09",
      "position": " ",
      "role": " ",
      "desc": " ",
      "image": " ",
      "employer": " ",
      "employer_link": " ",
      "supervisor": " ",
      "supervisor_link": " ",
      "visible": true
    });
    this.setState({ education });
  };

  handleEducationChange = (index, key, value) => {
    const education = [...this.state.education];
    education[index][key] = value;
    this.setState({ education });
  };

  // Experience
  handleAddExperince = () => {
    const experience = [...this.state.experience];
    experience.push({       "experience_type": " ",
    "title": "",
    "start_date": "",
    "end_date": "",
    "position": "",
    "role": "",
    "desc": "",
    "image": "",
    "employer": "",
    "employer_link": "",
    "supervisor": " ",
    "supervisor_link": " ",
    "visible": true
});
    this.setState({ experience });
  };

  handleExperienceChange = (index, key, value) => {
    const experience = [...this.state.experience];
    experience[index][key] = value;
    this.setState({ experience });
  };

  handleTemplateChange = (event) => {
    const template = event.target.value;
    this.setState({
      template: template
    });
  };
  
  handleSubmit = (event) => {
    event.preventDefault();
    // Do something with the form data
    fetch('http://localhost:8050/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.state)
    })
      .then(response => {console.log(JSON.stringify(this.state)); response.json()})
      .then(data => console.log(data))
      .catch(error => console.error(error));

  };



  render(){
    return(
      <Container>
        <Form onSubmit={this.handleSubmit}>

          <Row>

            <Col>
              <Form.Group controlId="username">
              <Form.Label>Username:</Form.Label>
              <Form.Control type="text" value={this.state.username} onChange={(event) => this.setState({ username: event.target.value })} />
              </Form.Group>
            </Col>

            <Col>
              <Form.Group controlId="password">
              <Form.Label>Password:</Form.Label>
              <Form.Control type="password"  value={this.state.password} onChange={(event) => this.setState({ password: event.target.value })} />
              </Form.Group>
            </Col>


            <Col>
              <Form.Group controlId="name">
              <Form.Label>Name:</Form.Label>
              <Form.Control type="text" value={this.state.name} onChange={(event) => this.setState({ name: event.target.value })} />
              </Form.Group>
            </Col>

            <Col>
            <Form.Group controlId="email">
            <Form.Label>Email</Form.Label>
            <Form.Control type="email" value={this.state.email} onChange={(event) => this.setState({ email: event.target.value })} />
            </Form.Group>
            </Col>
          </Row>
         

          <Row>

            <Col>
            <Form.Group controlId="phone">
            <Form.Label>Phone Number</Form.Label>
            <Form.Control type="tel" value={this.state.phone} onChange={(event) => this.setState({ phone: event.target.value })} />
            </Form.Group>            
            </Col>

            <Col>
            <Form.Group controlId="city">
            <Form.Label>City</Form.Label>
            <Form.Control type="text" value={this.state.city} onChange={(event) => this.setState({ city: event.target.value })} />
            </Form.Group>
            </Col>

            <Col>
            <Form.Group controlId="github">
            <Form.Label>GitHub URL</Form.Label>
            <Form.Control type="url" value={this.state.github} onChange={(event) => this.setState({ github: event.target.value })} />
            </Form.Group>
            </Col>
          </Row>

         <Row>

          <Col>
          <Form.Group controlId="profile-img">
            <Form.Label>Profile Image URL</Form.Label>
            <Form.Control type="url" value={this.state.profileImg} onChange={(event) => this.setState({ profileImg: event.target.value })} />
          </Form.Group>
          </Col>

          <Col>
          <Form.Group controlId="cover-img">
            <Form.Label>Cover Image URL</Form.Label>
            <Form.Control type="url" value={this.state.coverImg} onChange={(event) => this.setState({ coverImg: event.target.value })} />
          </Form.Group>
          </Col>

          <Col>
          <Form.Group controlId="thumbnail-img">
            <Form.Label>Thumbnail Image URL</Form.Label>
            <Form.Control type="url" value={this.state.thumbnailImg} onChange={(event) => this.setState({ thumbnailImg: event.target.value })} />
          </Form.Group>
          </Col>

         </Row>

        <Row>
          <Col>
            <Form.Group controlId="bio">
              <Form.Label>Bio</Form.Label>
              <Form.Control as="textarea" onChange={(event) => this.setState({ bio: event.target.value })} />
            </Form.Group>
          </Col>
        </Row>



          <hr />
          <Form.Group controlId="skills">
            <Form.Label>Skills</Form.Label>
            {/* value={this.state.skills.join('\n')} */}
            <Form.Control as="textarea" rows={3}  onChange={(event) => this.setState({ skills: {"skill_name":event.target.value} })} />
          </Form.Group>

          <hr />

          {/* Education Section */}
          <Form.Group>
            <Form.Label>Education</Form.Label>
            {this.state.education.map((edu, index) => (
              <div key={index}>
                <Row>
                  <Col>
                    <Form.Control type="text" placeholder="Degree" value={edu.title} onChange={(event) => this.handleEducationChange(index, 'title', event.target.value)} />
                  </Col>
                  
                  <Col>
                    <Form.Control type="text" placeholder="Institution" value={edu.employer} onChange={(event) => this.handleEducationChange(index, 'employer', event.target.value)} />
                  </Col>

                  <Col>
                    <Form.Control type="text" placeholder="Start Date" value={edu.start_date} onChange={(event) => this.handleEducationChange(index, 'start_date', event.target.value)} />
                  </Col>

                  <Col>
                    <Form.Control type="text" placeholder="End Date" value={edu.end_date} onChange={(event) => this.handleEducationChange(index, 'end_date', event.target.value)} />
                  </Col>
                </Row>
                <br />
              </div>
            ))}
            <Button variant="secondary" onClick={this.handleAddEducation}>Add Education</Button>
          </Form.Group>

          <hr />
          
          {/* Experience Section */}
          {/* experience: [{ position: '', company: '', startdate: '', enddate: '', description: ''}]*/}
          <Form.Group>
            <Form.Label>Experience</Form.Label>
            {this.state.experience.map((exp, index) => (
              <div key={index}>
                <Row>
                  <Col>
                    <Form.Control type="text" placeholder="Position" value={exp.role} onChange={(event) => this.handleExperienceChange(index, 'role', event.target.value)} />
                  </Col>
                  
                  <Col>
                    <Form.Control type="text" placeholder="Employer" value={exp.employer} onChange={(event) => this.handleExperienceChange(index, 'employer', event.target.value)} />
                  </Col>
                  
                  <Col>
                    <Form.Control type="text" placeholder="Start Date" value={exp.start_date} onChange={(event) => this.handleExperienceChange(index, 'start_date', event.target.value)} />
                  </Col>

                  <Col>
                    <Form.Control type="text" placeholder="End Date" value={exp.end_date} onChange={(event) => this.handleExperienceChange(index, 'end_date', event.target.value)} />
                  </Col>

                </Row>

                <Row>
                  <Col>
                    <Form.Control as="textarea" placeholder="Description" value={exp.desc} onChange={(event) => this.handleExperienceChange(index, 'desc', event.target.value)} />
                  </Col>
                </Row>
                <br />
              </div>
            ))}
            <Button variant="secondary" onClick={this.handleAddExperince}>Add Experience</Button>
          </Form.Group>

          <hr />

          {/* Projects Section */}
          <Form.Group>
            <Form.Label>Projects</Form.Label>
            {this.state.projects.map((project, index) => (
              <div key={index}>
                <Row>
                  <Col>
                    <Form.Control type="text" placeholder="Title" value={project.title} onChange={(event) => this.handleProjectChange(index, 'title', event.target.value)} />
                  </Col>
                  
                  <Col>
                    <Form.Control type="url" placeholder="Link" value={project.other_link} onChange={(event) => this.handleProjectChange(index, 'other_link', event.target.value)} />
                  </Col>
                </Row>

                <Row>
                  <Col>
                    <Form.Control as="textarea" placeholder="Description" value={project.short_desc} onChange={(event) => this.handleProjectChange(index, 'short_desc', event.target.value)} />
                  </Col>
                </Row>
                <br />
              </div>
            ))}
            <Button variant="secondary" onClick={this.handleAddProject}>Add Project</Button>
          </Form.Group>

          <hr />
          
          {/* Template Choice */}

          {/* <div className='template-choice'>
            <input type="radio" name="templates" value="1" id="temp1" checked={this.state.template === "1"} onChange={(event) => this.setState({ template: event.target.value })}/>
            <label htmlFor="temp1"> 
              <img className='choice-img' src='https://gcdnb.pbrd.co/images/28ys453DmZQm.png'></img> 
            </label>

            <input type="radio" name="templates" value="2" id="temp2" checked={this.state.template === "2"} onChange={(event) => this.setState({ template: event.target.value })}/>
            <label htmlFor="temp2"> <img className='choice-img' src='https://gcdnb.pbrd.co/images/IDtGlz4Nnivk.png'></img></label>
          </div> */}
         

          
          <br/>

          <Button variant="primary" type="submit">Submit</Button>
        </Form>
      </Container>
    )
  }
}

export default App;
