import React, { useState } from 'react'
import { Formik, Form, Field } from 'formik';
import { contactSend } from '../../api/contactSend'
import { ContactFormValidationSchema } from './ContactFormValidationSchema'


export default function ContactForm() {
  const [status, setStatus] = useState("idle")

  function formSubmit(values) {
    setStatus("loading")
    contactSend(values)
      .then(() => setStatus("succeeded"))
  }

  if (status === "idle") {
    return (
      <div>
        <h1>Contact Us</h1>
        <Formik
          initialValues={{
            author: '',
            title: '',
            body: '',
            category: 1,
          }}
          validationSchema={ContactFormValidationSchema}
          onSubmit={(values) => formSubmit(values)}
        >
        {({ errors, touched }) => (
          <Form>
            <Field type="email" name="author"/><br/>
            {errors.author && touched.author && <div>{errors.author}</div>}
            <Field name="title"/><br/>
            {errors.title && touched.title && <div>{errors.title}</div>}
            <Field name="body" as="textarea"/><br/>
            {errors.body && touched.body && <div>{errors.body}</div>}
            <Field name="category" as="select">
              <option value="1">Cooperation Proposal</option>
            </Field><br/>
            <button type="submit">
              Submit
            </button>
          </Form>
        )}
        </Formik>
      </div>
    )
  } else if (status === "loading") {
    return(
      <div>Loading</div>
    )
  } else if (status === "succeeded") {
    return (
      <div>
        Thank you for contacting with us
      </div>
    )
  }
}
