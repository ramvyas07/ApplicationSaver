import React from 'react';

function Home() {
  return (
    <div >
      <form action="/" method="POST">
            <label>
                Company Name: 
                <input type="text" name='application_name' id='application_name' required />
            </label>
            <label>
                Application Link: 
                <input type="text" name='application_link' id='application_link' required />
                        </label>
            <label>
                status: 
                <input type="text" name='application_status' id='application_status' required />
            </label>
                <input type="submit" value="Submit" name="formSubmit" />
      </form>
    </div>
  );
}

export default Home;