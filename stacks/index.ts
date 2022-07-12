import { App } from "@serverless-stack/resources";
import { Api } from "./Api";

export default function main(app: App) {
  app.setDefaultFunctionProps({
    runtime: "python3.9",
    srcPath: "services",
  });
  app.stack(Api)
}
