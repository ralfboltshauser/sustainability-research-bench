import Explorer from '../../ui';
export default async function Page({params}){const {slug}=await params;return <Explorer slug={slug}/>}
