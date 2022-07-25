import { App } from "@serverless-stack/resources";
import { Api } from "./Api";

export default function main(app: App) {
  app.setDefaultFunctionProps({
    runtime: "python3.8",
    srcPath: "services",
  });
  app.stack(Api)
} 
