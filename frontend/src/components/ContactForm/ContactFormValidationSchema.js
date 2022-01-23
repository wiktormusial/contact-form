import * as Yup from 'yup';


export const ContactFormValidationSchema = Yup.object().shape({
  author: Yup.string()
    .email('Must be a valid email')
    .max(255, 'Too Long!')
    .required('Required'),
  title: Yup.string()
    .min(3, 'Too Short!')
    .max(255, 'Too Long!')
    .required('Required'),
  body: Yup.string()
    .min(3, 'Too Short!')
    .required('Required'),
});
